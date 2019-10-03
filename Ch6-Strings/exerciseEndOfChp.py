def extractFloat(str):
    atpos = str.find(':')
    return float(str[atpos+1:len(str)])


if __name__ == '__main__':
    str = 'X-DSPAM-Confidence:0.8475'
    message = 'The float value is %g .' % extractFloat(str)
    print(message)

