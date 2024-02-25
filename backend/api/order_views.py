from .imports import *

@api_view(['GET'])
def orderView(request):
    order = Order.objects.all()
    seri = OrderSerializer(order,many=True)
    return Response(seri.data,status=200)

@api_view(['POST'])
def orderCreate(request):
    seri = OrderSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=400)
    
@api_view(['GET'])
def orderDetail(request,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Exception:
        return Response({"message":"nothing"},status=400)
    seri = OrderSerializer(order)
    return Response(seri.data,status=200)
    
@api_view(['PUT'])
def orderUpdate(request,order_id):
    try:
        order = Order.objects.get(id = order_id)
    except Exception:
        return Response({"message":"nothing"},status=400)
    seri = OrderSerializer(order,data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=400)
    
@api_view(['DELETE'])
def orderDelete(request,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Exception:
        return Response({"message":"nothing"},status=400)
    order.delete()
    return Response({"message":"delete"},status=200)