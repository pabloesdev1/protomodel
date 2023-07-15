from protomodel import message, service, rpc


@message
class Product:
    id: int
    name: str
    price: float
    brand_id: int
    category_id: int
    enabled: bool


@message
class GetProductRequest:
    product_id: int


@message
class GetProductResponse:
    product: Product


@message
class GetProductsResponse:
    products: list[Product]


@service
class ProductService:

    @rpc
    def get_product(get_product_request: GetProductRequest, other_param: int) -> GetProductResponse:
        ...
