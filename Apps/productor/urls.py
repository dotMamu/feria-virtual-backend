from .views import *
from django.urls import path, include
from rest_framework import routers
router  = routers.DefaultRouter()
# router.register(r'createSale', VentaLocalViewSet)


urlpatterns = [
     path('createOffer/', AddOfferView.as_view()),
     path('createSale/', CreateLocalSaleView.as_view()),
     path('uploadImage/', LocalSaleImageView.as_view()),
     path("seeAllOffer/",SeeAllOfferView.as_view()),
     path("searchOffer/",SearchOfferView.as_view()),
     path("searchSale/",SearchSaleView.as_view()),
     path("closeSale/",CloseSaleView.as_view()),
     path("cancelOffer/",CancelOfferView.as_view()),
     path("seeAllSales/",SeeAllLocalSalesView.as_view()),
     path("acceptBid/", AcceptDeclineAssignmentView.as_view()),
     path("packageTrackingGeneral/",ShippingStatusGeneralView.as_view()),
     path("packageTrackingProducer/", ShippingStatusProducerView.as_view()),
     path("confirmPreparation/",MarkShipping.as_view()),
     path("restockLocalSale/",RestockLocalSale.as_view()),
     path("retrieveImages/", RetrieveImagesView.as_view()),
     path("salesWithBuyingOffers/", SeeAllSalesWithBuyingOfferView.as_view()),
     path("updateOffer/", UpdateOffer.as_view()),
     path("updateSale/", UpdateSale.as_view()),
     path("seeAllBid/", SeeAllBidsView.as_view()),

   

]