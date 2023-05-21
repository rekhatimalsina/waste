from Customer.models import AddBins


def getBoinsId(id):
    bins = AddBins.objects.get(id= id)
    return bins

def updateBins(request,id):
    bins=AddBins.objects.get(id=id)
    bins.status=request.POST['status']
    bins.save()
    return "sucess"