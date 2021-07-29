import json

from django.core import serializers
from django.http import JsonResponse, HttpResponseNotFound

from todo.models import TodoRepository


def all(request):
    def read():
        result_json = json.loads(serializers.serialize('json', TodoRepository.all()))
        return JsonResponse(result_json, safe=False)

    def create():
        body = json.loads(request.body)
        todo = TodoRepository.create(
            title=body.get('title'),
            description=body.get('description')
        )
        result_json = json.loads(serializers.serialize('json', TodoRepository.filter(pk=todo.pk)))
        return JsonResponse(result_json, status=201, safe=False)

    def delete():
        TodoRepository.all().delete()
        return read()

    if request.method == 'GET':
        return read()
    elif request.method == 'POST':
        return create()
    elif request.method == 'DELETE':
        return delete()
    else:
        return HttpResponseNotFound()


def by_id(request, id):
    def read():
        result_json = json.loads(serializers.serialize('json', TodoRepository.filter(pk=id)))
        return JsonResponse(result_json, safe=False)

    def update():
        body = json.loads(request.body)
        TodoRepository.filter(pk=id).update(
            title=body.get('title'),
            description=body.get('description')
        )
        return read()

    def delete():
        TodoRepository.filter(pk=id).delete()
        return JsonResponse({})

    if request.method == 'GET':
        return read()
    elif request.method == 'PUT':
        return update()
    elif request.method == 'DELETE':
        return delete()
    else:
        return HttpResponseNotFound()
