from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
import json

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order = Order.objects.create(
                customer_name=data['customer_name'],
                phone=data['phone'],
                address=data['address'],
                total_amount=data['total_amount'],
                items=json.dumps(data['items'])
            )
            
            # Create the response
            response = JsonResponse({'message': 'Order saved!', 'order_id': order.id}, status=201)
            # FORCE the CORS headers (This fixes the "Unable to connect" error)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            
            return response
            
        except Exception as e:
            print("ERROR:", e) 
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Only POST requests allowed'}, status=400)