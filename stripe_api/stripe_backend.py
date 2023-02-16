import os
import stripe


class Stripe:
    def __init__(self):
        self.publish_key = os.getenv("stripe_publicKey")
        stripe.api_key = os.getenv("stripe_secretKey")

        self.currency = "eur"

    def view_apiKey(self):
        return self.publish_key

    def product_create(self, _name: str, _amount: int, _description: str):
        request = stripe.Product.create(name=_name,
                                        default_price_data={
                                            "currency": f"{self.currency}",
                                            "unit_amount_decimal": _amount
                                        },
                                        description=_description)
        return request

    def session_create(self, _price_id: str, _quantity: int):
        request = stripe.checkout.Session.create(
            success_url="https://www.google.com/search?q=good",
            line_items=[
                {
                    "price": f"{_price_id}",
                    "quantity": _quantity,
                }
            ],
            mode="payment")
        return request

    def session_retrieve(self, _session_id: str):
        request = stripe.checkout.Session.retrieve(_session_id)
        return request


if __name__ == "__main__":
    pass
