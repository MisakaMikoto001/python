"""
    推导式
        用来生成列表、集合、字典
"""
def formula_of_derivation():
    prices = {
        "APL":120.2,
        "AML":110.1,
        "PLO":89.4,
        "EOL":111.9,
        "TPL":9,
        "ROL":134
    }

    """
        {key_expression: value_expression for item in iterable if condition}
            parameters  key_expression and value_pression is the key-value for the new dict
                        for item in iterable is traversal_part, extract the object from the iterator
                        if condition is filter criteria ,only elements that satisfy the condition will be hold on
    """
    filtered_prices = {key:value for key,value in prices.items() if value < 100}

    print(filtered_prices)

"""
嵌套列表
"""
def nested_list():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']



def main():
    # formula_of_derivation()


    pass


if __name__ == '__main__':
    main()