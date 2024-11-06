from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=2000,default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAACUCAMAAAAH411kAAAAMFBMVEXHx8f////ExMT6+vr39/fLy8vR0dHs7Ozg4ODp6enOzs7W1tbZ2dnBwcHm5ubx8fH/Yo8tAAADVElEQVR4nO2a25ajIBBFtQDvyP//7YCIVpQYZ6bbFGud/dKdhAe2xaUorCoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeAgyUzeab/fih6DR1XU9frsbechWprKW7ra3nfIy/W926Z8hM9cBPTfVPaGl/Xxb/lEaXSfa6Y5PH5r2FAZcO0hz2mU8rrEfmtMi03oLO6lay7Khrn5BzXTZQdsuMuG/Tt54s7o+oJurHm6RWWbPMt6e6uodjjI+PBc6i4wLS0eIkfNbDjUPdvYj6qyj383tOGecITJhw1G+HTW6ExSdjE14+DniHAsycR0cQmRUreTY0GneBLKPm5plHHqZKTwCNdL6lRwbO+dsVLZtG21sl4xpDFr606L+HPHpnpjOzzt23XfeLX/67ZvLNfBhKDdxcs/7dWdyPjLT+1H5LSg/1DJd7LltlWTa57t8xZANTqZhy2QbWkPlhJ1y8sE5tzPMRhsbI1MLk/HbemaRzmWT3Fq3acBJY50AL8yZVeDcTIvKalZsf+pndgC5QyMlUaZ6meCR8f1+80FZAOakc9o+YzrDh9nwla7egKrjwqYOm+Jp1vTiDtGc8biydXwh2CKztnJCy08Jn+b3Wik9mxQFFp0tMnOoC3ajkRyXFWuJLFU2JWRd+mFL0UIZgOi6ciCOmXW+YjJ9WRorlJa4PsydLVbCEszb2KQTjmRz0ZEJrNHpmUypkQks++nMNiInq3D2t7hliU5DTpewKF9gOr9ap0TTFS4TNpYtfXtbLyyHXaYuPjLsTHpVmC4EJjMSjWUL0X7lFmRU0fGhgcsYFS8ECoXVc71MrLipTDW3CMI9xopXSGEqVIfVM0I6MKYPapJzG3Abu3U/HnBYOb286LB6xnpas7uOqAuBG3CZ9B27sipLhw0r/iLNrpOp6YqFybQ8CtRnJYXDZF5/oLY8nX1AnW6ZmE5bxNxhkz13MeOYjnwf9vTzt0xMR+r1wAa7J8iX/+PrKGkgyo4Ok3mX/fM7ReE67G2At8OInROE1wr3FODiIMN0hL1ndyCNIpW5JNyh7e0C2SMt5WeXMvtpQXo2HXU+yCQd+cknDa2+8chpcvJeHM5BtyrnZApIBQAAAAAAAAAAAAAAAAAAAAAAAAAAwH/wB7YkExPk+tZVAAAAAElFTkSuQmCC")


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})