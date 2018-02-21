import sys
import cv2

def test_patterns():
    img = cv2.imread("test.bmp", cv2.IMREAD_GRAYSCALE)

    img_out = {
        'BG2BGR': cv2.cvtColor(img, cv2.COLOR_BayerBG2BGR),
        'GB2BGR': cv2.cvtColor(img, cv2.COLOR_BayerGB2BGR),
        'RG2BGR': cv2.cvtColor(img, cv2.COLOR_BayerRG2BGR),
        'GR2BGR': cv2.cvtColor(img, cv2.COLOR_BayerGR2BGR),
        'BG2RGB': cv2.cvtColor(img, cv2.COLOR_BayerBG2RGB),
        'GB2RGB': cv2.cvtColor(img, cv2.COLOR_BayerGB2RGB),
        'RG2RGB': cv2.cvtColor(img, cv2.COLOR_BayerRG2RGB),
        'GR2RGB': cv2.cvtColor(img, cv2.COLOR_BayerGR2RGB)
    }
    
    for key, value in img_out.items():
        cv2.imwrite(key + '.jpg', value)

def convert(img_list):
    for img in img_list:
        print('test')

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Error, please specify a file or ptest. Use --help for more options.")
        exit()

    elif sys.argv[1] == 'ptest':
        test_patterns()

    elif sys.argv[1] == '--help':
        print("Commands:\n    ptest\n    convert [IMAGES]\n")

    elif sys.argv[1] == 'convert':
        convert(sys.argv[2:])
    
