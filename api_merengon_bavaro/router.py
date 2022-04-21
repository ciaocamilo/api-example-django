from merengon_api.viewsets import ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewset)

# http://localhost:8000/api/product/
# GET, POST, PUT, DELETE