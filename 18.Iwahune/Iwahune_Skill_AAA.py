Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      ModifyUnitShields(All, " * Samir Duran", CurrentPlayer, "Anywhere", 100);
      ModifyUnitHitPoints(All, " * Samir Duran", CurrentPlayer, "Anywhere", 100);
   },
}

for i = 0, 7, 1 do

radius = i / 4 * math.pi;

d = 50;
interval = 50;

i_x = math.sin(radius) * interval;
i_y = math.cos(radius) * interval;
i_x = math.floor(i_x + 0.5);
i_y = math.floor(i_y + 0.5);

x1 = math.sin(radius) * interval - i_y;
y1 = math.cos(radius) * interval + i_x;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * interval + i_y;
y2 = math.cos(radius) * interval - i_x;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 7, 1 do

radius = -i / 4 * math.pi;

d = 50;
interval = 50;

i_x = math.sin(radius) * interval;
i_y = math.cos(radius) * interval;
i_x = math.floor(i_x + 0.5);
i_y = math.floor(i_y + 0.5);

x1 = math.sin(radius) * interval - i_y;
y1 = math.cos(radius) * interval + i_x;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * interval + i_y;
y2 = math.cos(radius) * interval - i_x;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3 * i + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 24, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

radius = 1 / 4 * math.pi;

d = 50;
interval = 50;

i_x = math.sin(radius) * interval;
i_y = math.cos(radius) * interval;
i_x = math.floor(i_x + 0.5);
i_y = math.floor(i_y + 0.5);

x1 = math.sin(radius) * interval - i_y;
y1 = math.cos(radius) * interval + i_x;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * interval + i_y;
y2 = math.cos(radius) * interval - i_x;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

radius = 3 / 4 * math.pi;

d = 50;
interval = 50;

i_x = math.sin(radius) * interval;
i_y = math.cos(radius) * interval;
i_x = math.floor(i_x + 0.5);
i_y = math.floor(i_y + 0.5);

x1 = math.sin(radius) * interval - i_y;
y1 = math.cos(radius) * interval + i_x;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * interval + i_y;
y2 = math.cos(radius) * interval - i_x;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(4, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", Attack, "18.Iwahune");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "Zerg Queen", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "Zerg Queen", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "Zerg Queen", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

interval = 50;

x1 = interval * i;
y1 = interval + interval * i;

x2 = interval + interval * i;
y2 = interval * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, - interval, interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -2 * interval, -interval);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(AllPlayers, SetTo, 18001, " `SkillText_Uiltimate");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

radius = i / 4 * math.pi;

d = 50;
interval = 50;

i_x = math.sin(radius) * interval;
i_y = math.cos(radius) * interval;
i_x = math.floor(i_x + 0.5);
i_y = math.floor(i_y + 0.5);

x1 = math.sin(radius) * interval - i_y;
y1 = math.cos(radius) * interval + i_x;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * interval + i_y;
y2 = math.cos(radius) * interval - i_x;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Atmost, 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 3 * i, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x1, y1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x1, -y1);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Atmost, 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 3 * i + 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x2, y2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, i_x, i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x2, -y2);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -i_x, -i_y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Atmost, 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 3 * i + 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Atmost, 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 34, 1 do

radius = i / 64 * math.pi;

d = 320 - 8 * i;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, x, y);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -x, -y);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -y, x);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, y, -x);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 35, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -4 * interval, 4 * interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 8, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -9 * interval, -interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("18.Iwahune", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(170, -4 * interval, 4 * interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 8, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(9, "130 + 1n Norad", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "18.Iwahune");
      LMove(170, -9 * interval, -interval);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(500);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetAllianceStatus(P8, Enemy);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetAllianceStatus(P7, Enemy);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}
