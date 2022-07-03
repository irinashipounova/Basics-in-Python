import json

with open('text_7.txt', 'r', encoding='utf-8') as firm_info, open('text_77.json', 'w', encoding='utf-8') as firm_res:
    profit_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in firm_info}
    profit_pos = [i for i in profit_dict.values() if i > 0]
    profit_avg = round(sum(profit_pos) / len(profit_pos))
    result_dict = [profit_dict, profit_avg]

    json.dump(result_dict, firm_res, ensure_ascii=False, indent=4)
