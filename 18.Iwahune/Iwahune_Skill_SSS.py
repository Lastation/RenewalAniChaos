interval = 32;

x1 = -64;
y1 = 96;

x2 = -96;
y2 = 64;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      Wait(120);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


interval = 32;

x1 = 64;
y1 = 96;

x2 = 96;
y2 = 64;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      Wait(120);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(950);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      CreateUnit(1, "Kakaru (Twilight)", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


interval = 32;

x1 = -64;
y1 = 96;

x2 = -96;
y2 = 64;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


interval = 32;

x1 = 64;
y1 = 96;

x2 = 96;
y2 = 64;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -interval, -interval);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}



for i = 0, 3, 1 do

interval = 32;

x1 = interval * i;
y1 = interval + interval * i;

x2 = interval + interval * i;
y2 = interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y1, -x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y2, -x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y1, x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y2, x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, - interval, interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}