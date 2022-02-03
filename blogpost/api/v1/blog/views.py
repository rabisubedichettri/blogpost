from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.db.models import Q

from blog.models import Post
from .serializers import PostListSerializer
from rest_framework.decorators import api_view, permission_classes
from .permission import IsOwnerOrReadOnly


class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsOwnerOrReadOnly | IsAdminUser]

    def get_queryset(self):
        prams = self.request.query_params
        active = prams.get('published', True)
        user = prams.get('user', False)
        mine = prams.get('mine', False)
        order = prams.get('order', "ascending")

        check_authenticated = self.request.user.is_authenticated
        if check_authenticated:
            check_admin = self.request.user.is_superuser
        else:
            check_admin=False

        # creator cases
        if check_admin and check_authenticated == True and mine == True:
            queryset_parm = Q(active=active, user=self.request.user)

        # admin cases
        elif check_admin:
            queryset_parm = Q(active=active)
            if user:
                queryset_parm += Q(user__id=user)

        else:
            # random user (unauthenticated) cases
            queryset_parm = Q(active=True)

        # ordering
        if order == "ascending":
            queryset = Post.objects.filter(queryset_parm).order_by('published_at')
        else:
            queryset = Post.objects.filter(queryset_parm).order_by('-published_at')
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
