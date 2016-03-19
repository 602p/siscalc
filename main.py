import browser

class Category(object):
    def __init__(self, *a, **k):
        self.container=browser.html.DIV()
        self.assignments_container=browser.html.DIV()
        self.percent=browser.html.INPUT(readonly=True)
        self.weight=browser.html.INPUT(type="number")
        self.add=browser.html.BUTTON("Add Assignement")
        self.delete_this=browser.html.BUTTON("X")
        self.container<=browser.html.INPUT(value="Category")
        self.container<=" Weight:"
        self.container<=self.weight
        self.container<=" "
        self.container<=self.percent
        self.container<=self.add
        self.container<=" "
        self.container<=self.delete_this
        self.container<=browser.html.BR()
        self.container<=self.assignments_container
        browser.document.getElementById("categories_container")<=self.container

        self.add.bind("click", self.add_assignment)
        self.delete_this.bind("click", self.remove_this)
        self.weight.bind("input", self.update)

        categories.append(self)

        self.assignments=[]

    def register_assignement(self, assignment):
        self.assignments.append(assignment)

    def update(self, *a, **k):
        sum_score=sum([float(a.score.value) for a in self.assignments])
        sum_max=sum([float(a.max.value) for a in self.assignments])
        self._sum_max=sum_max
        self._percent=(sum_score/sum_max)*100
        self.percent.value=str(self._percent)+"%"
        _update_class()

    def _delete(self, a):
        self.assignments.remove(a)
        self.update()

    def remove_this(self, *a, **k):
        self.container.clear()
        categories.remove(self)

    def add_assignment(self, *a, **k):
        Assignment(self)

class Assignment(object):
    def __init__(self, parent):
        self.container=browser.html.DIV("-->")
        self.score=browser.html.INPUT(type="number")
        self.max=browser.html.INPUT(type="number")
        self.percent=browser.html.INPUT(readonly=True)
        self.remove=browser.html.BUTTON("X")
        self.as_pct=browser.html.BUTTON("%")
        self.container<=browser.html.INPUT(value="Assignment")
        self.container<=":"
        self.container<=self.score
        self.container<="/"
        self.container<=self.max
        self.container<=self.percent
        self.container<=self.remove
        self.container<=self.as_pct
        self.container<=browser.html.BR()
        self.parent=parent
        self.parent.assignments_container<=self.container

        self.score.bind("input", self.update)
        self.max.bind("input", self.update)
        self.remove.bind("click", self.delete)
        self.as_pct.bind("click", self.alert_as_pct)

        self.parent.register_assignement(self)

    def alert_as_pct(self, *a, **k):
        browser.alert("This assignement is "+str((float(self.max.value)/self.parent._sum_max)*100*float(self.parent.weight.value))+"% of your overall grade")

    def update(self, *a, **k):
        self.percent.value=str((float(self.score.value)/float(self.max.value))*100)+"%"
        self.parent.update()

    def delete(self, *a, **k):
        self.container.clear()
        self.parent._delete(self)

categories=[]

browser.document["add_category"].bind("click", Category)

def _update_class():
    print("foo")
    browser.document["class_pct"].value=str(sum([float(c.weight.value)*c._percent for c in categories]))+"%"
