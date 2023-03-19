# straight_rail.py
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from draftsman.constants import Direction
from draftsman.classes.collision_set import CollisionSet
from draftsman.classes.entity import Entity
from draftsman.classes.mixins import DoubleGridAlignedMixin, EightWayDirectionalMixin
from draftsman.utils import AABB, Rectangle
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import straight_rails
from draftsman.data import entities

import warnings

eps = 0.001
_vertical_collision = CollisionSet([AABB(-0.75, -1.0 + eps, 0.75, 1.0 - eps)])
_horizontal_collision = _vertical_collision.rotate(2)
_diagonal_collision = CollisionSet([Rectangle((-0.5, -0.5), 1.25, 1.40, 45)])
_collision_set_rotation = {}
_collision_set_rotation[Direction.NORTH] = _vertical_collision
_collision_set_rotation[Direction.NORTHEAST] = _diagonal_collision.rotate(2)
_collision_set_rotation[Direction.EAST] = _horizontal_collision
_collision_set_rotation[Direction.SOUTHEAST] = _diagonal_collision.rotate(4)
_collision_set_rotation[Direction.SOUTH] = _vertical_collision
_collision_set_rotation[Direction.SOUTHWEST] = _diagonal_collision.rotate(-2)
_collision_set_rotation[Direction.WEST] = _horizontal_collision
_collision_set_rotation[Direction.NORTHWEST] = _diagonal_collision

class StraightRail(DoubleGridAlignedMixin, EightWayDirectionalMixin, Entity):
    """
    A straight rail entity.
    """

    # fmt: off
    _exports = {
        **Entity._exports,
        **EightWayDirectionalMixin._exports,
        **DoubleGridAlignedMixin._exports,
    }
    # fmt: on

    def __init__(self, name=straight_rails[0], **kwargs):
        # type: (str, **dict) -> None
        """
        TODO
        """

        # This is kinda hacky, but necessary due to Factorio issuing dummy
        # values for collision boxes. We have to do this before initialization
        # of the rest of the class because certain things like tile position are
        # dependent on this information and can be set during initialization
        # (if we pass in arguments in **kwargs).

        # We set a (private) flag to ignore the dummy collision box that
        # Factorio provides
        self._overwritten_collision_set = True

        # We then provide a list of all the custom rotations
        self._collision_set = _vertical_collision
        self._collision_set_rotation = _collision_set_rotation

        super(StraightRail, self).__init__(name, straight_rails, **kwargs)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel=2,
            )

        del self.unused_args
