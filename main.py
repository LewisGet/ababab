import sys


SYMBOLS = [
    "啊", "吧", "額", "哦",
    "哈", "嘿", "咦", "嗚",
    "欸", "嗯", "呃", "？",
    "！", "，", "。", "～"
]


ENCODE_TABLE = dict()
DECODE_TABLE = dict()


index = 0
for i in SYMBOLS:
    for ii in SYMBOLS:
        two_words = i + ii
        ENCODE_TABLE[index] = two_words
        DECODE_TABLE[two_words] = index

        index += 1


def text_to_ababa(text: str) -> str:
    text = text.encode("utf-8")
    return ''.join(ENCODE_TABLE[i] for i in text)

def ababa_to_text(ababa_str: str) -> str:
    if len(ababa_str) % 2 != 0:
        raise ValueError("阿吧語長度必須是偶數！")

    # 每2個字元一組
    symbols = [ababa_str[i:i+2] for i in range(0, len(ababa_str), 2)]
    bytes_list = [DECODE_TABLE[i] for i in symbols]

    return bytes(bytes_list).decode('utf-8')

if __name__ == "__main__":
    try:
        input_str = sys.argv[1]
        encode = True if sys.argv[2] == "encode" or sys.argv[2] == "" else False

        if encode:
            result = text_to_ababa(input_str)
        else:
            result = ababa_to_text(input_str)

        print(result)
    except Exception as e:
        print("用法: python main.py <字串> [encode|decode]")
        print(e)
