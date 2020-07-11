from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import tcod.event

from actions import Action, BumpAction, EscapeAction

if TYPE_CHECKING:
    from engine import Engine


class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            # Update the FOV before the players next action
            self.engine.update_fov()

    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        key = event.sym
        player = self.engine.player

        if key in [tcod.event.K_UP, tcod.event.K_w]:
            action = BumpAction(player, dx=0, dy=-1)
        elif key in [tcod.event.K_DOWN, tcod.event.K_s]:
            action = BumpAction(player, dx=0, dy=1)
        elif key in [tcod.event.K_LEFT, tcod.event.K_a]:
            action = BumpAction(player, dx=-1, dy=0)
        elif key in [tcod.event.K_RIGHT, tcod.event.K_d]:
            action = BumpAction(player, dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        return action
