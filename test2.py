main_dct = {}
def many_dct(**kwargs):
    main_dct.update(**kwargs)
    return main_dct
many_dct(brand='Volvo', model='XC90', year=2022)
many_dct(sedan='Volkswagen', Coupe='Porsche')
many_dct(January='spring', June='summer')
many_dct(name='Vitalii', age=38, eyes_color='green')
print(main_dct)
