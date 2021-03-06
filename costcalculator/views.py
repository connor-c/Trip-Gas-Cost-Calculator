from django.shortcuts import render, redirect
from costcalculator.forms import *
from .distance import get_distance

def index(request):
    if request.method == 'POST':
        origin = OriginForm(request.POST)
        destination = DestinationForm(request.POST)
        gas_price = GasPriceForm(request.POST)
        mpg = MpgForm(request.POST)
        num_people = NumPeopleForm(request.POST)

        if origin.is_valid() and destination.is_valid() and gas_price.is_valid() and mpg.is_valid() and num_people.is_valid():
            forms = {'origin': origin.cleaned_data['origin_address'],
                     'destination': destination.cleaned_data['destination_address'],
                     'gas_price': gas_price.cleaned_data['gas_price'],
                     'mpg': mpg.cleaned_data['mpg'],
                     'num_people': num_people.cleaned_data['num_people']}

            request.session['completed_forms'] = forms
            return redirect('calculated_addresses/')
        else:
            if not origin.is_valid():
                origin = OriginForm(request.GET)
            if not destination.is_valid():
                destination = DestinationForm(request.GET)
            if not gas_price.is_valid():
                gas_price = GasPriceForm(request.GET)
            if not mpg.is_valid():
                mpg = MpgForm(request.GET)
            if not num_people.is_valid():
                num_people = NumPeopleForm(initial={'num_people':1})

            return render(request, 'costcalculator/index.html', {'origin':origin,
                                                                 'destination':destination,
                                                                 'gas_price':gas_price,
                                                                 'mpg':mpg,
                                                                 'num_people':num_people})

    else:
        origin = OriginForm(request.GET)
        destination = DestinationForm(request.GET)
        gas_price = GasPriceForm(request.GET)
        mpg = MpgForm(request.GET)
        num_people = NumPeopleForm(initial={'num_people':1})

        return render(request, 'costcalculator/index.html', {'origin':origin,
                                                             'destination':destination,
                                                             'gas_price':gas_price,
                                                             'mpg':mpg,
                                                             'num_people':num_people})


def calculated(request):
    completed_forms = request.session.get('completed_forms')

    if request.method == 'POST':
        origin = OriginForm(request.POST)
        destination = DestinationForm(request.POST)
        gas_price = GasPriceForm(request.POST)
        mpg = MpgForm(request.POST)
        num_people = NumPeopleForm(request.POST)

        if origin.is_valid() and destination.is_valid() and gas_price.is_valid() and mpg.is_valid() and num_people.is_valid():
            completed_forms = {'origin': origin.cleaned_data['origin_address'],
                     'destination': destination.cleaned_data['destination_address'],
                     'gas_price': gas_price.cleaned_data['gas_price'],
                     'mpg': mpg.cleaned_data['mpg'],
                     'num_people': num_people.cleaned_data['num_people']}

            request.session['completed_forms'] = completed_forms

    try:
        distance = get_distance(completed_forms['origin'], completed_forms['destination'])
    except KeyError:
        distance = None
    trip_cost = 'Distance Calculation Error, Please Try Again.'
    cost_per_person = 'Distance Calculation Error, Please Try Again.'

    if distance is not None:
        trip_cost = round((distance / completed_forms['mpg']) * completed_forms['gas_price'], 2)
        cost_per_person = '$' + str(round(trip_cost / completed_forms['num_people'], 2))
        distance = str(round(distance, 1)) + ' miles'
        trip_cost = '$' + str(trip_cost)
    else:
        distance = 'Distance Calculation Error, Please Try Again.'

    origin = OriginForm(initial={'origin_address':completed_forms['origin']})
    destination = DestinationForm(initial={'destination_address':completed_forms['destination']})
    gas_price = GasPriceForm(initial={'gas_price':completed_forms['gas_price']})
    mpg = MpgForm(initial={'mpg':completed_forms['mpg']})
    num_people = NumPeopleForm(initial={'num_people':completed_forms['num_people']})

    return render(request, 'costcalculator/calculated_addresses.html', {'origin':origin,
                                                                        'destination':destination,
                                                                        'gas_price':gas_price,
                                                                        'mpg':mpg,
                                                                        'num_people':num_people,
                                                                        'distance':distance,
                                                                        'trip_cost':trip_cost,
                                                                        'cost_per_person': cost_per_person})


def use_distance(request):
    if request.method == 'POST':
        distance = DistanceForm(request.POST)
        gas_price = GasPriceForm(request.POST)
        mpg = MpgForm(request.POST)
        num_people = NumPeopleForm(request.POST)

        if distance.is_valid() and gas_price.is_valid() and mpg.is_valid() and num_people.is_valid():
            forms = {'distance': distance.cleaned_data['distance'],
                     'gas_price': gas_price.cleaned_data['gas_price'],
                     'mpg': mpg.cleaned_data['mpg'],
                     'num_people': num_people.cleaned_data['num_people']}

            request.session['completed_forms'] = forms
            return redirect('../calculated_distance/')
        else:
            if not distance.is_valid():
                distance = DistanceForm(request.GET)
            if not gas_price.is_valid():
                gas_price = GasPriceForm(request.GET)
            if not mpg.is_valid():
                mpg = MpgForm(request.GET)
            if not num_people.is_valid():
                num_people = NumPeopleForm(initial={'num_people':1})

            return render(request, 'costcalculator/use_distance.html', {'distance':distance,
                                                                        'gas_price':gas_price,
                                                                        'mpg':mpg,
                                                                        'num_people':num_people})
    else:
        distance = DistanceForm(request.GET)
        gas_price = GasPriceForm(request.GET)
        mpg = MpgForm(request.GET)
        num_people = NumPeopleForm(initial={'num_people':1})

        return render(request, 'costcalculator/use_distance.html', {'distance':distance,
                                                                    'gas_price':gas_price,
                                                                    'mpg':mpg,
                                                                    'num_people':num_people})


def calculated_distance(request):
    completed_forms = request.session.get('completed_forms')

    if request.method == 'POST':
        distance = DistanceForm(request.POST)
        gas_price = GasPriceForm(request.POST)
        mpg = MpgForm(request.POST)
        num_people = NumPeopleForm(request.POST)

        if distance.is_valid() and gas_price.is_valid() and mpg.is_valid() and num_people.is_valid():
            completed_forms = {'distance': distance.cleaned_data['distance'],
                               'gas_price': gas_price.cleaned_data['gas_price'],
                               'mpg': mpg.cleaned_data['mpg'],
                               'num_people': num_people.cleaned_data['num_people']}

            request.session['completed_forms'] = completed_forms

    trip_cost = round((completed_forms['distance'] / completed_forms['mpg']) * completed_forms['gas_price'], 2)
    cost_per_person = '$' + str(round(trip_cost / completed_forms['num_people'], 2))
    calculated_distance = str(round(completed_forms['distance'], 1)) + ' miles'
    trip_cost = '$' + str(trip_cost)

    distance = DistanceForm(initial={'distance':completed_forms['distance']})
    gas_price = GasPriceForm(initial={'gas_price':completed_forms['gas_price']})
    mpg = MpgForm(initial={'mpg':completed_forms['mpg']})
    num_people = NumPeopleForm(initial={'num_people':completed_forms['num_people']})

    return render(request, 'costcalculator/calculated_distance.html', {'gas_price':gas_price,
                                                                       'mpg':mpg,
                                                                       'num_people':num_people,
                                                                       'distance':distance,
                                                                       'calculated_distance':calculated_distance,
                                                                       'trip_cost':trip_cost,
                                                                       'cost_per_person':cost_per_person})
