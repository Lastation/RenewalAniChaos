
for i = 0, 7, 1 do 

for j = 0, 7, 1 do

radius1 = j / 4 * math.pi;
radius2 = radius1 + 1 / 12 * math.pi;
radius3 = radius1 - 1 / 12 * math.pi;

d = 50 + i * 20;
interval = 20;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x1_a = math.sin(radius1) * (d + interval);
y1_a = math.cos(radius1) * (d + interval);
x1_a = math.floor(x1 + 0.5);
y1_a = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

x2_a = math.sin(radius2) * (d + interval);
y2_a = math.cos(radius2) * (d + interval);
x2_a = math.floor(x2 + 0.5);
y2_a = math.floor(y2 + 0.5);

x3 = math.sin(radius3) * d;
y3 = math.cos(radius3) * d;
x3 = math.floor(x3 + 0.5);
y3 = math.floor(y3 + 0.5);

x3_a = math.sin(radius3) * (d + interval);
y3_a = math.cos(radius3) * (d + interval);
x3_a = math.floor(x3 + 0.5);
y3_a = math.floor(y3 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 9 + j, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(3, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = false,
         intransit = false,
         hallucinated = false,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });
      CreateUnit(3, "60 + 1n Archon", "[Skill]Unit_Wait_2", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1_a, y1_a);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2_a, y2_a);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x3, y3);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x3_a, y3_a);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");

      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 9 + 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 72, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


radius1 = 1 / 4 * math.pi;
radius2 = math.pi;

d = 210;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      Wait(2500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}