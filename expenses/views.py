from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class ExpenseListView(generic.ListView):
    model = Expense
    template_name = 'expenses/list.html'
    context_object_name = 'expenses'
    
    def get_queryset(self):
        return Expense.objects.all().order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = sum(e.amount for e in context["expenses"])
        context['form'] = ExpenseForm()
        return context


    
def delete_expenses(request, pk): 
    expense = get_object_or_404(Expense, pk = pk)
    expense.delete()
    return redirect('expenses:expense_list')



class ExpenseCreateView(generic.CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses:expense_list')
    
    def form_invalid(self, form):
        expenses = Expense.objects.all().order_by('-date')
        return render(self.request, 'expenses/list.html',{
            'expenses': expenses,
            'total' : sum(e.amount for e in expenses),
            'form': form
        })
        

class ExpenseDeleteView(generic.DeleteView):
    model = Expense
    success_url= reverse_lazy('expenses:expense_list')