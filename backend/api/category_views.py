from .imports import *

@api_view(['GET'])
def categoryView(request):
    category = Category.objects.all()
    seri = CategorySerializer(category,many=True)
    return Response(seri.data,status=200)

@api_view(['POST'])
def categoryCreate(request):
    seri = CategorySerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=404)
    
@api_view(['GET'])
def categoryDetail(request,cate_id):
    try:
        category = Category.objects.get(id=cate_id)
    except Exception:
        return Response({"message":"Nothing"},status=500)
    seri = CategorySerializer(category)
    return Response(seri.data,status=200)

@api_view(['PUT'])
def categoryUpdate(request,cate_id):
    try:
        category = Category.objects.get(id=cate_id)
    except Exception:
        return Response({"message":"Nothing"},status=404)
    seri = CategorySerializer(category,data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=404)
    
@api_view(['DELETE'])
def categoryDelete(request,cate_id):
    try:
        category = Category.objects.get(id=cate_id)
    except Exception:
        return Response({"message":"NOthing"},status=500)
    category.delete()
    return Response({"message":"Delete"},status=200)
    
