
for i = 0, 3, 1 do

d = 40 + 40 * i;

radius1 = 1 / 4 * math.pi;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
radius2 = 0 / 4 * math.pi;

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y1, x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y1, -x1);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x2, y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x2, -y2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y2, x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y2, -x2);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Guardian", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 7, 1 do

d = 50;

radius1 = i / 4 * math.pi;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x1, y1);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x1, -y1);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}