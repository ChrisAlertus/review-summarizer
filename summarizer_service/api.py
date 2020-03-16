from flask import Flask, request, jsonify, make_response
from helpers import load_artefacts, get_word_indexes, process_review, decode_sequence

app = Flask(__name__)

max_text_len = 30
max_summary_len = 8
encoder_model, decoder_model, x_tokenizer, y_tokenizer = load_artefacts("artefacts")
reverse_target_word_index, reverse_source_word_index, target_word_index = get_word_indexes(x_tokenizer, y_tokenizer)


@app.route("/summarize", methods=['POST'])
def summarize():
    req = request.get_json()
    review = req["review"]
    review_tokenized = process_review(review, max_text_len, x_tokenizer, encoder_model, decoder_model)
    summary = "".join([i + " " for i in decode_sequence(review_tokenized,
                                                        encoder_model,
                                                        decoder_model,
                                                        target_word_index,
                                                        reverse_target_word_index,
                                                        max_summary_len).
                      strip(" ").
                      split(" ")[1:]])
    return make_response(jsonify({"summary": summary}), 200)


app.run(host='127.0.0.1', port=5000, debug=True)
