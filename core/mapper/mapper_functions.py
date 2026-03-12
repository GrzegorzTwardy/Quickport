import pandas as pd
from exceptions.mapper_exceptions import UnknownMappingTypeError
from core.mapper.mapper_model import ProductFieldMapping

pd.set_option('future.no_silent_downcasting', True)
mapping_functions_list = ['SET ALL', 'PRICE', 'REPLACE', 'JOIN', 'FRAGMENT']


# UTILITY FUNCTIONS
def cell(column: pd.Series, row: int):
    return column[row]


# COLUMN MAPPING FUNCTIONS
# each returns -> tuple(pd.Series, pd.Series)
#              -> mapped_values, invalid_mask   

# get price 0.00 format from col
def price(column: pd.Series, conversion_factor: float):
    # pd.Series of validated prices (true - valid price, false - not valid)
    matches = column.astype(str).str.match(r'^\d+(\.\d{1,2})?$')

    values = pd.Series(index=column.index, dtype='float')
    values[matches] = column[matches].astype(float) * conversion_factor

    formatted = values.map(lambda x: format(x, '.2f') if pd.notna(x) else None)
    
    invalid_mask = ~matches
    return formatted, invalid_mask


# set all column rows with provided text 
def set_all(target_index: pd.Index, text: str):
    values = pd.Series(text, index=target_index)
    invalid_mask = pd.Series(False, index=target_index)
    return values, invalid_mask


# replaces values X in column with values Y
def replace_values(column: pd.Series, mapping: dict[str, str]):
    
    def str_conversion(val):
        if pd.isna(val):
            return val
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        return str(val)
    
    # using values from dataframe as strings
    str_column = column.map(str_conversion)
    
    values = str_column.replace(mapping)
    invalid_mask = pd.Series(False, index=column.index)
    return values, invalid_mask


# joins n columns with a separator
def join(columns: list[pd.Series], separator: str, null_display=None):
    values = columns[0].astype('string')

    for col in columns[1:]:
        values = values.str.cat(col.astype('string'), sep=separator, na_rep=null_display)

    invalid_mask = pd.Series(False, index=values.index)
    return values, invalid_mask


def get_fragment(column: pd.Series, separator: str, part: int):
    try:
        i = part - 1
        values = column.astype(str).str.split(separator).str[i]
        invalid_mask = pd.Series(False, index=column.index)
        return values, invalid_mask
    except Exception as e:
        return None, None


# APPLYING MAPPINGS FROM MODEL OBJECT
def apply_mapping_function(df, mapping: ProductFieldMapping) -> tuple[pd.Series, pd.Series]:
    
    mapping_type = mapping.mapping_type
    args = mapping.args
    
    match mapping_type:
        case 'SET ALL':
            return set_all(df.index, args['text'])
        case 'PRICE':
            src_column = args['source_column']
            cf = args['conversion_factor']
            return price(df[src_column], cf)
        case 'REPLACE':
            src_column = args['source_column']
            value_mapping = args['value_mapping']
            return replace_values(df[src_column], value_mapping)
        case 'JOIN':
            column_names = args['source_columns']
            source_columns = [df[col] for col in column_names if col in df.columns]
            separator = args['separator']
            null_display = args.get('null_display', None)
            return join(source_columns, separator, null_display)
        case 'FRAGMENT':
            src_column = args['source_column']
            separator = args['separator']
            part = int(args['part'])
            return get_fragment(df[src_column], separator, part)
        case _:
            raise UnknownMappingTypeError(mapping_type)
     

if __name__ == '__main__':
    df = pd.DataFrame(
        [['text1', 'v1', 0, 'x-y-z'], 
        ['text2', 'v2', 1, 'x-y-z'], 
        ['text3', 'v3', 2, 'x-y-z']], 
        columns=['COL1', 'COL2', 'COL3', 'COL4']
    )

    mapping = ProductFieldMapping(
        included=True,
        sf_target_field='test',
        source_column='test',
        mapping_type='FRAGMENT',
        allows_nulls=True,
        args={
            'source_column': 'COL4',
            'separator': '-',
            'part': 2
        }
    )
    
    df['COL4'],_ = apply_mapping_function(df, mapping)
    
    print(df)