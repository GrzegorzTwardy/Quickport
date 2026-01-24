import pandas as pd
from exceptions.mapper_exceptions import UnknownMappingTypeError
from core.mapper.mapper_model import ProductFieldMapping

mapping_functions_list = ['SET ALL', 'PRICE', 'REPLACE', 'JOIN']

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

    # values - [4.234234, 0.4342, NaN]
    values = pd.Series(index=column.index, dtype='float')
    values[matches] = column[matches].astype(float) * conversion_factor

    # mapped [4.23, 0.43, None]
    formatted = values.map(lambda x: format(x, '.2f') if pd.notna(x) else None)
    
    invalid_mask = ~matches
    return formatted, invalid_mask


# set all column rows with provided text 
def set_all(column: pd.Series, text: str):
    values = pd.Series(text, index=column.index)
    invalid_mask = pd.Series(False, index=column.index) # invalid mapping not possible
    return values, invalid_mask


# replaces values X in column with values Y
def replace_values(column: pd.Series, mapping: dict[str, str]):
    values = column.replace(mapping)
    invalid_mask = pd.Series(False, index=column.index)
    return values, invalid_mask


# joins n columns with a separator
def join(columns: list[pd.Series], separator: str, null_default=None):
    values = columns[0].astype('string')

    for col in columns[1:]:
        values = values.str.cat(col.astype('string'), sep=separator, na_rep=null_default)

    invalid_mask = pd.Series(False, index=values.index)
    return values, invalid_mask


# APPLYING MAPPINGS FROM MODEL OBJECT
def apply_mapping_function(df, mapping: ProductFieldMapping) -> tuple[pd.Series, pd.Series]:
    
    mapping_type = mapping.mapping_type
    args = mapping.args
    
    match mapping_type:
        case 'SET ALL':
            src_column = args['source_column']
            return set_all(df[src_column], args['text'])
        case 'PRICE':
            src_column = args['source_column']
            cf = args['conversion_factor']
            return price(df[src_column], cf)
        case 'REPLACE VALUES':
            src_column = args['source_column']
            value_mapping = args['value_mapping']
            return replace_values(df[src_column], value_mapping)
        case 'JOIN':
            column_names = args['source_columns']
            source_columns = [df[col] for col in column_names if col in df.columns]
            separator = args['separator']
            null_default = args['null_default']
            return join(source_columns, separator, null_default)
        case _:
            raise UnknownMappingTypeError(mapping_type)
     

if __name__ == '__main__':
    df = pd.DataFrame(
        [['text1', 'v1', 0], 
        ['text2', 'v2', 1], 
        ['text3', 'v3', 2]], 
        columns=['COL1', 'COL2', 'COL3']
    )
    
    mapping = {
        'mapping_type': 'SET ALL',
        'args': {
            'column': 'COL2',
            'text': 'NEW TEXT'
        }
    }
    
    df['COL2'] = apply_mapping_function(df, mapping)
    
    print(df)