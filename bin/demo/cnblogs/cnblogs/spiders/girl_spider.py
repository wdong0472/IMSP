
import scrapy, json
from ..items import TuchongItem

class PhotoSpider(scrapy.Spider):
    name = 'photo'
    # allowed_domains = ['tuchong.com']
    # start_urls = ['http://tuchong.com/']

    def start_requests(self):
        url = 'https://tuchong.com/rest/tags/%s/posts?page=%d&count=20&order=weekly';
        # 抓取10个页面，每页20个图集
        # 指定 parse 作为回调函数并返回 Requests 请求对象
        for page in range(1, 11):
            yield scrapy.Request(url=url % ('美女', page), callback=self.parse)

    # 回调函数，处理抓取内容填充 TuchongItem 属性
    def parse(self, response):
        body = json.loads(response.body_as_unicode())
        items = []
        for post in body['postList']:
            
            # 不符合条件触发 scrapy.exceptions.DropItem 异常，符合条件的输出地址
            if int(item['image_count']) < 3:
                raise DropItem("美女太少: " + item['url'])
            elif item['type'] != 'multi-photo':
                raise DropItem("格式不对: " + + item['url'])
            else:
                print(item['url'])
        
            item = TuchongItem()
            item['type'] = post['type']
            item['post_id'] = post['post_id']
            item['site_id'] = post['site_id']
            item['title'] = post['title']
            item['url'] = post['url']
            item['excerpt'] = post['excerpt']
            item['image_count'] = int(post['image_count'])
            item['images'] = {}
            # 将 images 处理成 {img_id: img_url} 对象数组
            for img in post.get('images', ''):
                img_id = img['img_id']
                url = 'https://photo.tuchong.com/%s/f/%s.jpg' % (item['site_id'], img_id)
                item['images'][img_id] = url

            item['tags'] = []
            # 将 tags 处理成 tag_name 数组
            for tag in post.get('tags', ''):
                item['tags'].append(tag['tag_name'])
            items.append(item)
        return items

