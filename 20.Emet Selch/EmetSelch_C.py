

for i = 0, 1, 1 do

radius1 = i / 4 * math.pi;

d1 = 96;

x1 = math.sin(radius1) * d1;
y1 = math.cos(radius1) * d1;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

d3 = 128;

x3 = math.sin(radius1) * d3;
y3 = math.cos(radius1) * d3;
x3 = math.floor(x3 + 0.5);
y3 = math.floor(y3 + 0.5);


radius2 = i / 4 * math.pi;

d2 = 120;

x2 = math.sin(radius2) * d2;
y2 = math.cos(radius2) * d2;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

d4 = 160;

x4 = math.sin(radius2) * d4;
y4 = math.cos(radius2) * d4;
x4 = math.floor(x4 + 0.5);
y4 = math.floor(y4 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Drone", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x1, y1);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x1, -y1);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y1, x1);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y1, -x1);
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x3, y3);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x3, -y3);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y3, x3);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y3, -x3);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x2, y2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x2, -y2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y2, x2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y2, -x2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x4, y4);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x4, -y4);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y4, x4);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y4, -x4);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Drone", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(200);
      KillUnitAt(All, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

x1 = 50;
y1 = 0;

x2 = 100;
y2 = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x1, y1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x1, -y1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y1, x1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y1, -x1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x2, y2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x2, -y2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y2, x2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y2, -x2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(120);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      Wait(0);
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x1, y1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x1, -y1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y1, x1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y1, -x1);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x2, y2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x2, -y2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y2, x2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y2, -x2);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mutalisk", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      Wait(120);
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}