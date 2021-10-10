from .init_nn import responce_nn
import numexpr as ne


def parser_and_calculator(responce):
    resp = responce_nn(responce)
    awd = forward_to_num(resp).replace(',', '+')
    return ne.evaluate(awd)


def forward_to_num(resp):
    gkae = seach_num(resp[0].split())
    sfesgs = dfgsrg(gkae)
    return alnefks(sfesgs, gkae[1]) 


def seach_num(resp):
    numbers = []
    numb = ''
    sequrense = ''
    for i in resp:
        try:
            n = int(i)
            numb += str(i) + ' '
            sequrense += '0'
        except:
            if sequrense != '':
                numbers.append(numb[:-1])
            numb = ''
            if i == 'sqrt':
                sequrense += ' ' + '**(1/2)' + ' '
            elif i == '^':
                sequrense += ' ' + '**' + ' '
            elif i == 'log':
                sequrense += ' ' + 'np.log' + ' '
            else:
                sequrense += ' ' + str(i) + ' '
    if numb != '':
        numbers.append(numb[:-1])
    return numbers, sequrense


def bild_num(seq):
    num_umn = 0
    num_sum = 0
    deliteli = ['1000', '100000', '1000000', '1000000000', '1000000000000', '1000000000000000']
    for i in seq.split():
        if i in deliteli:
            if num_sum == 0:
                num_umn += int(i)
            else:
                num_umn += num_sum*int(i)
            num_sum = 0
        else:
            num_sum += int(i)
    if num_sum != 0:
        num_umn += num_sum
    return num_umn


def dfgsrg(mas_numb):
    awdf = []
    for i in mas_numb[0]:
        awdf.append(bild_num(i))
    return awdf


def alnefks(awdf, mas_numb):
    sequerents = ''
    ad = 0
    for i in mas_numb.split():
        try:
            int(i)
            sequerents += str(awdf[ad]) 
            ad += 1
        except:
            sequerents +=  i
    return sequerents


if __name__=='__main__':
    print(parser_and_calculator('пять умножить на три'))