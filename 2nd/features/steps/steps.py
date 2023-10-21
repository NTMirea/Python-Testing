from behave import *
from twentyone import *


@given('дилер')
def step_impl(context):
    context.dealer = Dealer()


@given('рука с итогом {total:d}')
def step_impl(context, total):
    context.dealer = Dealer()
    context.total = total


@given('{hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')


@when('дилер суммирует карты')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()


@when('начинается раунд')
def step_impl(context):
    context.dealer.new_round()


@when('дилер определяет свой ход')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)


@then('дилер берет себе две карты')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)


# NEW STEP
@then('дилер выбирает ход')
def step_impl(context):
    assert (context.dealer.make_play() in ['stand', 'hit'])


@then('{total:d} верен')
def step_impl(context, total):
    assert (context.dealer_total == total)


@then('{play} верен')
def step_impl(context, play):
    assert (context.dealer_play == play)
