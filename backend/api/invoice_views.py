from .imports import *

@api_view(['GET'])
def invoiceView(request):
    invoice = Invoice.objects.all()
    seri = InvoiceSerializer(invoice,many=True)
    return Response(seri.data,status=200)

@api_view(['POST'])
def invoiceCreate(request):
    seri = InvoiceSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=404)
    
@api_view(['GET'])
def invoiceDetail(request,in_id):
    try:
        invoice = Invoice.objects.get(id=in_id)
    except Exception:
        return Response({"message":"nothing"},status=500)
    seri = InvoiceSerializer(invoice)
    return Response(seri.data,status=200)

@api_view(['PUT'])
def invoiceUpdate(request,in_id):
    try:
        invoice = Invoice.objects.get(id=in_id)
    except Exception:
        return Response({"message":"nothing"},status=500)
    seri = InvoiceSerializer(invoice,data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=200)
    else:
        return Response(seri.errors,status=404)

@api_view(['DELETE'])
def invoiceDelete(request,in_id):
    try:
        invoice = Invoice.objects.get(id=in_id)
    except Exception:
        return Response({"message":"nothing"},status=500)
    invoice.delete()
    return Response({"message":"delete"},status=200)
    