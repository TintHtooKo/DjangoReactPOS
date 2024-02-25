from .imports import *

@api_view(['GET'])
def productView(request):
    product = Product.objects.all()
    seri = ProductSerializer(product,many=True)
    return Response(seri.data,status=200)

@api_view(['POST'])
def productCreate(request):
    seri = ProductSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=404)
    
@api_view(['GET'])
def productDetail(request,pro_id):
    try:
        product = Product.objects.get(id=pro_id)
    except Exception:
        return Response({"message":"NOthing"},status=400)
    seri = ProductSerializer(product)
    return Response(seri.data,status=200)

@api_view(['PUT'])
def productUpdate(request,pro_id):
    try:
        product= Product.objects.get(id=pro_id)
    except Exception:
        return Response({"message":"nothing"},status=400)
    seri = ProductSerializer(product,data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=400)
    
@api_view(['DELETE'])
def productDelete(request,pro_id):
    try:
        product = Product.objects.get(id=pro_id)
    except Exception:
        return Response({"message":"nothing"},status=400)
    product.delete()
    return Response({"message":"delete"},status=200)