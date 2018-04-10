from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# post model. Functional structure of the application.

class Post(models.Model):
	post_title = models.CharField(max_length=150)
	post_content = models.TextField()
	post_createdOn = models.DateTimeField('date published')
	post_author = models.TextField()
	post_slug = models.SlugField(unique=True, max_length=255)

	def __str__(self):
		return self.post_title

@models.permalink
def get_absolute_url(self):
 	return ('blog_post_detail', (),
          {
             'post_slug': self.slug,
          })

def save(self, *args, **kwargs):
     if not self.slug:
         self.slug = slugify(self.post_title)
         super(Post, self).save(*args, **kwargs)

class Meta:
        ordering = ['createdOn']

        def __unicode__(self):
            return self.post_title


# comments model. One post can get any comments

class Comment(models.Model):
	comm_name = models.CharField(max_length=50)
	comm_content = models.TextField()
	comm_createOn = models.DateTimeField(auto_now_add=True)
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)