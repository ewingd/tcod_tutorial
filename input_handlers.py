from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        key = event.sym

        if key in [tcod.event.K_UP, tcod.event.K_w]:
            action = MovementAction(dx=0, dy=-1)
        elif key in [tcod.event.K_DOWN, tcod.event.K_s]:
            action = MovementAction(dx=0, dy=1)
        elif key in [tcod.event.K_LEFT, tcod.event.K_a]:
            action = MovementAction(dx=-1, dy=0)
        elif key in [tcod.event.K_RIGHT, tcod.event.K_d]:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
