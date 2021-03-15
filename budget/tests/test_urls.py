from django.test import SimpleTestCase # TestCase클래스의 서브클래스 더 풍부한 기능을 갖고 있음
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list') # url을 만들어줌
        print(resolve(url))   # MatchObject를 반환함
        self.assertEquals(resolve(url).func, project_list) # 즉, `list` name인 url 정확히 해당 url을 호출하는지 확인하게됨.
        
    def test_add_url_is_resolved(self):
        url = reverse('add') 
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)  # view_class를 CBV인 경우에 첫번째 인자의 꽁무니에 붙여야함.

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=['some-slug'])             # url에 argument를 집어 넣어야하는 경우 필요함
        self.assertEquals(resolve(url).func, project_detail)  
