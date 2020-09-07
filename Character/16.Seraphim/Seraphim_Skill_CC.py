
for i = 0, 3, 1 do

radius = i / 8 * math.pi;

d1 = 70;
d2 = 130;

x1 = math.sin(radius) * d1;
y1 = math.cos(radius) * d1;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * d2;
y2 = math.cos(radius) * d2;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x1, y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y1, x1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y1, -x1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 100;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

radius1 = 1 / 4 * math.pi;
radius2 = 2 / 4 * math.pi;

d = 130;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x1, y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y1, x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y1, -x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y2, x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y2, -x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 70;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 10, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x1, y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y1, x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y1, -x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 11, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y2, x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y2, -x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x1 = 50;
y1 = 50;

x2 = 100;
y2 = 100;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x1, y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y1, x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y1, -x1);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y2, x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y2, -x2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
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