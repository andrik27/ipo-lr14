import json
import os
from django.http import JsonResponse
from django.conf import settings

def load_data():
    """Загрузка данных из JSON файла"""
    file_path = os.path.join(settings.BASE_DIR, 'dump.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def spec_list(request):
    """Список всех навыков (skills)"""
    data = load_data()
    
    skills = [
        {
            'id': item['pk'],
            'code': item['fields']['code'],
            'title': item['fields']['title'],
            'specialty_id': item['fields']['specialty'],
            'url': f"/spec/{item['pk']}/"
        }
        for item in data 
        if item['model'] == 'data.skill' 
    ]
    
    return JsonResponse(skills, safe=False)

def spec_detail(request, pk):
    """Детальная информация о навыке"""
    data = load_data()
    
    try:
        item = next(
            item for item in data 
            if item['model'] == 'data.skill' and item['pk'] == pk
        )
        
        return JsonResponse({
            'id': item['pk'],
            'code': item['fields']['code'],
            'title': item['fields']['title'],
            'specialty_id': item['fields']['specialty'],
            'description': item['fields'].get('desc'),
            'search_tag': item['fields'].get('searchtag')
        })
        
    except StopIteration:
        return JsonResponse({'error': 'Навык не найден'}, status=404)