from .forms import NewsletterForm


def subscription_form(request):
    """Make Newsletter Subscription Form available throughout all the pages"""
    newsletter_form = NewsletterForm()
    context = {
        'newsletter_form': newsletter_form,
        }
    return context
