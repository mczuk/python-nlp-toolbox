import argparse
import logging
import xml.etree.ElementTree as ET


def ccl2iob2(ccl: str) -> [str]:
    ccl_tree = ET.fromstring(ccl)
    lines = []

    for sentence in ccl_tree.iter("sentence"):
        prev_id = 0
        for token in sentence.iter("tok"):
            orth = token.find("orth").text
            lemma = token.find("lex").find("base").text
            ctag = token.find("lex").find("ctag").text
            ne_lemma = "-"
            ne_label = "O"
            ne_eid = "-"

            for ann in token.iter("ann"):
                if ann.text != "0":
                    ne_label = ann.attrib["chan"]
                    if prev_id == ann.text:
                        ne_label = "I-" + ne_label
                    else:
                        ne_label = "B-" + ne_label
                    prev_id = ann.text

            for prop in token.iter("prop"):
                type = prop.attrib['key'].split(":")[1]
                if type == "lemma":
                    ne_lemma = prop.text
                elif type == "eid":
                    ne_eid = prop.text

            lines.append(f"{orth}\t{lemma}\t{ctag}\t{ne_lemma}\t{ne_eid}\t{ne_label}")
        lines.append("")

    return lines


def main(path_input: str, path_output: str):
    content = open(path_input).read()
    lines = ccl2iob2(content)

    if path_output:
        pass
    else:
        print(*lines, sep="\n")


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert set of IOB files into a single json file in PolEval 2018 NER format')
    parser.add_argument('--input', required=True, metavar='PATH', help='path to an input file in CCL format')
    parser.add_argument('--output', required=False, metavar='PATH', help='path to an output file. Default: stdout')
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filemode="w")
    args = parse_args()
    try:
        main(args.input, args.output)
    except ValueError as er:
        print("[ERROR] %s" % er)