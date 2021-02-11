"""Basic unit tests for Lambdata package"""

from random import randint
import pytest
import lambdata as ld

def inc(x):
    return x + 1

def test_inc():
    ans = inc(3)
    assert ans == 4

def test_increment_int():
    """Making sure increment works"""
    x0 = 0
    y0 = ld.increment_int(x0) # 1
    assert y0 == 1

    x1 = 100
    y1 = ld.increment_int(x1) #101
    assert y1 == 101

def test_increment_float():
    """Making sure increment works for floats"""
    x0 = 10.5
    y0 = ld.increment_int(x0) # 11.5
    assert y0 == 11.5

def test_increment_neg_int():
    """Making sure increment works for negative integers"""
    x0 = -1
    y0 = ld.increment_int(x0) # 1
    assert y0 == 0

def test_increment_neg_float():
    """Making sure increment works for negative floats"""
    x0 = -1.5
    y0 = ld.increment_int(x0) # -0.5
    assert y0 == -0.5


# Testing OOP_examples

user1 = SocialMediaUser(ld.oop_examples.SocialMediaUser(
    name="Nick", location="Arizona"))
user2 = SocialMediaUser(ld.oop_examples.SocialMediaUser(
    name="Carl", location="Costa Rica", upvotes=250))

def test_SMU_constructor():
    """Testing that name works properly"""
    # testing name
    assert user1.name.lower() == "nick"
    assert user2.name.lower() == 'carl'
    # testing location
    assert user1.location.lower() == "arizona"
    assert user2.location.lower() == "costa rica"
    # testing upvotes
    assert user1.upvotes == 0
    assert user2.upvotes == 250


