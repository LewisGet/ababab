import sys


ENCODE_TABLE = {
    0: "阿阿",  1: "阿吧",  2: "阿？",  3: "阿！",
    4: "阿，",  5: "阿。",  6: "吧阿",  7: "吧吧",
    8: "吧？",  9: "吧！", 10: "吧，", 11: "吧。",
   12: "？阿", 13: "？吧", 14: "？？", 15: "？！"
}

DECODE_TABLE = {v: k for k, v in ENCODE_TABLE.items()}

def text_to_ababa(text: str) -> str:
    ababa = []
    for char in text:
        # 取得 ASCII / UTF-8 的第一個 byte（僅支援 ASCII 字元）
        byte_val = ord(char)
        if byte_val > 255:
            raise ValueError(f"暫不支援非 ASCII 字元: {char}")
        # 拆成高4位和低4位
        high_nibble = (byte_val >> 4) & 0xF  # 高4位
        low_nibble  = byte_val & 0xF         # 低4位
        # 查表轉符號
        ababa.append(ENCODE_TABLE[high_nibble])
        ababa.append(ENCODE_TABLE[low_nibble])
    return ''.join(ababa)

def ababa_to_text(ababa_str: str) -> str:
    if len(ababa_str) % 2 != 0:
        raise ValueError("阿吧語長度必須是偶數！")

    # 每2個字元一組
    symbols = [ababa_str[i:i+2] for i in range(0, len(ababa_str), 2)]

    bytes_list = []
    for i in range(0, len(symbols), 2):
        if i + 1 >= len(symbols):
            raise ValueError("阿吧語符號數量需為4的倍數（每字元4符號）")
        high_sym = symbols[i]
        low_sym  = symbols[i+1]

        if high_sym not in DECODE_TABLE or low_sym not in DECODE_TABLE:
            raise ValueError(f"未知的阿吧符號: {high_sym} 或 {low_sym}")

        high_val = DECODE_TABLE[high_sym]
        low_val  = DECODE_TABLE[low_sym]
        byte_val = (high_val << 4) | low_val
        bytes_list.append(byte_val)

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
