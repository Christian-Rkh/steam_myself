import os
import random
from platform import processor

from flask import Flask, render_template, jsonify, request
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/coupons')
def get_coupons():
    return jsonify({"coupons": "1% 할인, 2% 할인"})


@app.route('/type')
def get_type():
    return jsonify({"type":"임시입력"})

@app.route("/order", methods=["post"])
def order():
    data = request.get_json()
    name = data.get("name")
    price = int(data.get("type"))
    type_name = data.get("type_name")
    coupon_id = data.get("coupon")

    final_price = price
    if coupon_id == 1 and type_name == "Demon Slayer: Kimetsu no Yaiba: Hinokami Blood Wind Story":
        final_price = price - 20
    elif coupon_id == 2 and type_name == "Geometry Dash":
        final_price = int(round(price * 0.2))

    msg = f"{name}님 주문 완료. 상품: {type_name}, 원가: {price}, 최종 결제 금액: {final_price}"

    return jsonify({"msg":msg})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))  # Render가 주는 PORT 사용
    app.run(host="0.0.0.0", port=port, debug=False)