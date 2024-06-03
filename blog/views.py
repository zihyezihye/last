from django.shortcuts import render

from .models import Blog
from .serializers import BlogSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
'''
전체 블로그를 조회
'''
# @api_view(['GET', 'POST']) # @는 데코레이터, 특정 요청만 받겠다는 의미=> 여기서는 GET요청만 받겠다
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])

# class BlogList(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get(self, request):
#         blogs = Blog.objects.all() #DB에서 블로그 모델의 객체를 가져오겠음. all()하면 전부 다 가져옴.
#         serializer = BlogSerializer(blogs, many=True) #여러개 객체를 바꿀때는 many=True 필수 #여기까진 파이썬 딕셔너리로 바뀜 #직렬화 순서 : 파이썬 클래스 - 파이썬 딕셔너리 - 제이슨
#         return Response(serializer.data) #이 단계에서 딕셔너리-> 제이슨으로 바뀜

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data) #제이슨-> 파이썬 객체로 가는 역직렬화
#         if serializer.is_valid(raise_exception=True): #데이터 저장하기 전에 꼭 거쳐야 하는 유효성 검사
#             serializer.save(user=request.user) #데이터가 DB에 저장됨 #user=request.user => 로그인했던 유저 객체를 블로그에 연결
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#                 #serializer.errors => 오류뜨면 해당 오류 메세지를 반환함



from rest_framework.generics import ListCreateAPIView

class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): #유저 연결
        user = self.request.user
        serializer.save(user=user)

#한 블로그 조회

# @api_view(['GET', 'PUT', 'DELETE']) 
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsOwnerOrReadOnly])

# from django.shortcuts import get_object_or_404

# class BlogDetail(APIView):
    
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]
    
    
#     def get_object(self, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         return blog

#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.generics import RetrieveUpdateDestroyAPIView

class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    