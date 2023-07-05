from protomodel import message, service, rpc

@message
class Product:
    id: int
    name: str
    brand_id: int
    price: float
    category_id: int


@message
class GetProductRequest:
    product_id: int

@message
class GetProductResponse:
    product: Product

@message
class GetProductsResponse:
    products: list[Product]
