from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'post_list.html'

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'