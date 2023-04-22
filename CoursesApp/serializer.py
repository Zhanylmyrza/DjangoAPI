from rest_framework import serializers
from CoursesApp.models import Category,Branch,Contact,Course


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Category
    fields=('id','name','impath')

class BranchSerializer(serializers.ModelSerializer):
  class Meta:
    model=Branch
    fields=('id','latitude','longitude','address')
    
class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model=Contact
    fields=('id','type')
    
class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model=Course
    fields=('id','name','description','logo','category')


