Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("19.M&N_Bozo2", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
   },
}

for i = 0, 3, 1 do

radius = i / 8 * math.pi;

d = 100;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(300);
      SetSwitch("Recall - M&N", Set);
      SetDeaths(P1, SetTo, 0, " `NarugeTarget");
      SetDeaths(P2, SetTo, 0, " `NarugeTarget");
      SetDeaths(P3, SetTo, 0, " `NarugeTarget");
      SetDeaths(P4, SetTo, 0, " `NarugeTarget");
      SetDeaths(P5, SetTo, 0, " `NarugeTarget");
      SetDeaths(P6, SetTo, 0, " `NarugeTarget");
      SetDeaths(AllPlayers, SetTo, 1004, " `SkillText4");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 24, 1 do

radius = i / 32 * math.pi;

d = 100 - 3 * i;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n High Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 25, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetSwitch("Recall - M&N", Clear);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x = -96;
y = 48;

i_x = 24;
i_y = -12;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(9, "Target", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 48;
y = 96;

i_x = -12;
i_y = -24;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(9, "Target", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 48;
y = -96;

i_x = -12;
i_y = 24;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(9, "Target", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


x = 96;
y = 48;

i_x = -24;
i_y = -12;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, "Protoss Dark Templar", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(9, "Target", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(9, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, i_x, i_y);
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Bring(P4, AtLeast, 1, "Any unit", "19.M&N_Bozo2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(P4, SetTo, 720, " `NarugeTarget");
   },
}
Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Bring(P5, AtLeast, 1, "Any unit", "19.M&N_Bozo2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(P5, SetTo, 720, " `NarugeTarget");
   },
}
Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Bring(P6, AtLeast, 1, "Any unit", "19.M&N_Bozo2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(P6, SetTo, 720, " `NarugeTarget");
   },
}
Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Bring(P1, AtLeast, 1, "Any unit", "19.M&N_Bozo2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(P1, SetTo, 720, " `NarugeTarget");
   },
}
Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Bring(P2, AtLeast, 1, "Any unit", "19.M&N_Bozo2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(P2, SetTo, 720, " `NarugeTarget");
   },
}
Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Bring(P3, AtLeast, 1, "Any unit", "19.M&N_Bozo2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(P3, SetTo, 720, " `NarugeTarget");
   },
}
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, AtLeast, 1, " `NarugeTarget");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `NarugeTarget");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
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