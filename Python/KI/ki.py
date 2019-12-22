import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim

done = False


class MeinNetz(nn.Module):
    def __init__(self):
        super(MeinNetz, self).__init__()
        self.lin1 = nn.Linear(10, 10)
        self.lin2 = nn.Linear(10, 10)

    def forward(self, x):
        x = F.relu(self.lin1(x))
        x = self.lin2(x)

        return x


netz = MeinNetz()


def train(ra, lr=0.221, s=0, ll=[], li=0):
    if os.path.isfile('meinNetz.pt'):
        os.remove('meinNetz.pt')

    try:
        for o in range(ra):
            s += 1
            if s > 10000 or s == 10000:
                torch.save(netz, 'meinNetz.pt')
                s = 0
            x = [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
            input = Variable(torch.Tensor([x for _ in range(10)]))

            out = netz(input)

            x = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
            target = Variable(torch.Tensor([x for _ in range(10)]))
            criterion = nn.MSELoss()
            loss = criterion(out, target)
            print('Epoch: [{}/{} ({}%)]  Loss: {}'.format(o, ra, 100. * o / ra, loss))

            netz.zero_grad()
            loss.backward()
            optimizer = optim.Adam(netz.parameters(), lr=lr)
            optimizer.step()
            ll.append(loss)
            li += 1
            if len(ll) > 100:
                ll.clear()
                li = 0

        print(out)
        torch.save(netz, 'meinNetz.pt')
        print('\n Training beendet!\n')
        print('Der durch schnitts loss wert ist: ' + str(cdl(li, ll)))
    except KeyboardInterrupt:
        print(out)
        torch.save(netz, 'meinNetz.pt')
        print('\n Training vorzeitig beendet\n')


def test_trained_netz():
    if os.path.isfile('meinNetz.pt'):
        netz = torch.load('meinNetz.pt')
    else:
        print('Du musst zuerst eine Ki Trainieren!')
        return

    x = [0, 1, 1, 1, 0, 1, 1, 1, 0 ,0]
    print(f'Input: {x}')
    print('Output: \n')
    input = Variable(torch.Tensor([x for _ in range(10)]))
    out = netz(input)
    print(out)


def cdl(li, ll, ll2=0):
    for i in range(li):
        ll2 += ll[i]

    return ll2 / li


while not done:
    print('1 Trainieren\n2 Testen')
    try:
        choice = int(input('Deine Entscheidung: '))

        if choice == 1:
            ra = int(input('Wie viele durch läufe soll deine KI haben? '))
            lr = float(input('Welche learning rate soll der Trainings vorgang haben (Standart: 0.221): '))
            if lr < 0 or lr == 0:
                print('Die learning rate darf nicht unter null sein/null sein!'
                      '\nEs wird jetzt mit dem Standart wert fortgefahren')
                lr = 0.221
            train(ra, lr)
            done = True
        elif choice == 2:
            test_trained_netz()
            done = True
        else:
            print('Du musst eine option wählen')
    except ValueError:
        print('Du musst eine Zahl eingeben')

"""
Bestes Ergebnis:
500000 durch läufe   Standart learning rate
Epoch: [499990/500000 (99.998%)]  Loss: 0.012524524703621864
Epoch: [499991/500000 (99.9982%)]  Loss: 0.01189996674656868
Epoch: [499992/500000 (99.9984%)]  Loss: 0.012524524703621864
Epoch: [499993/500000 (99.9986%)]  Loss: 0.01189996674656868
Epoch: [499994/500000 (99.9988%)]  Loss: 0.012524524703621864
Epoch: [499995/500000 (99.999%)]  Loss: 0.01189996674656868
Epoch: [499996/500000 (99.9992%)]  Loss: 0.012524524703621864
Epoch: [499997/500000 (99.9994%)]  Loss: 0.01189996674656868
Epoch: [499998/500000 (99.9996%)]  Loss: 0.012524524703621864
Epoch: [499999/500000 (99.9998%)]  Loss: 0.01189996674656868

Der durch schnitts loss wert ist: tensor(0.0122, grad_fn=<DivBackward0>)
"""
