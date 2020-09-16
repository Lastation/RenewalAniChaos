import Function as f;

function SkillUnitBurrowed(cp : TrgPlayer, count, Unit : TrgUnit);
function SquareShape(cp : TrgPlayer, count, Unit : TrgUnit, x, y);
function EdgeShapeBurrowed(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval);

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {
            f.SquareShape(cp, 1, "60 + 1n Siege", 50 * f.loop[cp] + 50, 0);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 50 * f.loop[cp] + 50, 50);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 50 * f.loop[cp] + 50, -50);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.SkillWait(cp, 480);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            var i = 0;
            for (; i < 4; i++)
            {  
               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50 * i + 50, 50);
               f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50 * i + 50, -50);
            }

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            var i = 0;
            for (; i < 4; i++)
            {  
               f.SquareShape(cp, 1, "Kakaru (Twilight)", 50 * i + 50, 50);
               f.SquareShape(cp, 1, "Kakaru (Twilight)", 50 * i + 50, -50);
            }

            f.SkillWait(cp, 2400);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            f.Voice_Routine(cp, 4);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("Kakaru (Twilight)", cp, "Anywhere", Move, f.location[cp]);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 8)
         {
            if (f.loop[cp] < 4)
            {
               f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
               EdgeShapeBurrowed(cp, 1, "Zerg Defiler", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
               KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            }
            else if (f.loop[cp] == 4)
            {
               f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 9, 200);
               KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            }

            CreateUnit(2, " Unit. Hoffnung 25000", dwrand() % 8 + 33, cp);
            CreateUnit(2, "Protoss Dark Archon", dwrand() % 8 + 33, cp);
            CreateUnit(4, "40 + 1n Mutalisk", dwrand() % 8 + 33, cp);
            CreateUnitWithProperties(4, "Unclean One (Defiler)", dwrand() % 8 + 33, cp, UnitProperty(burrowed=True));
            SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
            MoveLocation(f.location[cp], "Kakaru (Twilight)", cp, "Anywhere");
            RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Mutalisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Unclean One (Defiler)", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Kakaru (Twilight)", cp, "Anywhere");
            RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Mutalisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Protoss Dark Archon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Unclean One (Defiler)", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Kakaru (Twilight)", cp, "Anywhere");
            RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Mutalisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Unclean One (Defiler)", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Kakaru (Twilight)", cp, "Anywhere");
            RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Mutalisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Protoss Dark Archon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Unclean One (Defiler)", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);


            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 8)
         {
            CreateUnit(2, " Unit. Hoffnung 25000", dwrand() % 8 + 33, cp);
            CreateUnit(2, "Protoss Dark Archon", dwrand() % 8 + 33, cp);
            CreateUnit(4, "40 + 1n Guardian", dwrand() % 8 + 33, cp);
            CreateUnitWithProperties(4, "40 + 1n Zergling", dwrand() % 8 + 33, cp, UnitProperty(burrowed=True));
            SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
            MoveLocation(f.location[cp], "Unclean One (Defiler)", cp, "Anywhere");
            RemoveUnitAt(1, "Unclean One (Defiler)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Unclean One (Defiler)", cp, "Anywhere");
            RemoveUnitAt(1, "Unclean One (Defiler)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Protoss Dark Archon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Unclean One (Defiler)", cp, "Anywhere");
            RemoveUnitAt(1, "Unclean One (Defiler)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Unclean One (Defiler)", cp, "Anywhere");
            RemoveUnitAt(1, "Unclean One (Defiler)", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Protoss Dark Archon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);


            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] < 8)
         {
            CreateUnit(2, " Unit. Hoffnung 25000", dwrand() % 8 + 33, cp);
            CreateUnit(2, "Protoss Dark Archon", dwrand() % 8 + 33, cp);
            CreateUnit(4, "40 + 1n Guardian", dwrand() % 8 + 33, cp);
            SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
            MoveLocation(f.location[cp], "40 + 1n Zergling", cp, "Anywhere");
            RemoveUnitAt(1, "40 + 1n Zergling", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "40 + 1n Zergling", cp, "Anywhere");
            RemoveUnitAt(1, "40 + 1n Zergling", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Protoss Dark Archon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "40 + 1n Zergling", cp, "Anywhere");
            RemoveUnitAt(1, "40 + 1n Zergling", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "40 + 1n Zergling", cp, "Anywhere");
            RemoveUnitAt(1, "40 + 1n Zergling", "Anywhere", cp);
            MoveUnit(1, "40 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "Protoss Dark Archon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 640);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 5)
      {
         if (f.loop[cp] < 10)
         {
            CreateUnit(2, " Unit. Hoffnung 25000", dwrand() % 8 + 33, cp);
            CreateUnit(2, "40 + 1n Zergling", dwrand() % 8 + 33, cp);
            CreateUnit(4, " Creep. Licht", dwrand() % 8 + 33, cp);
            CreateUnit(8, "80 + 1n Guardian", dwrand() % 8 + 33, cp);
            SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Creep. Licht", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Creep. Licht", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Creep. Licht", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveLocation(f.location[cp], "Zerg Defiler", cp, "Anywhere");
            RemoveUnitAt(1, "Zerg Defiler", "Anywhere", cp);
            MoveUnit(1, "80 + 1n Guardian", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(1, " Creep. Licht", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

            KillUnitAt(All, "80 + 1n Guardian", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Unit. Hoffnung 25000", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(All, "40 + 1n Zergling", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(All, " Creep. Licht", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Unit. Hoffnung 25000", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Zergling", cp, "Anywhere", Attack, f.location[cp]);
            Order(" Creep. Licht", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 10)
         {
            f.SkillWait(cp, 1200);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 6)
      {
         KillUnitAt(All, "40 + 1n Zergling", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, " Creep. Licht", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}


function SkillUnitBurrowed(cp : TrgPlayer, count, Unit : TrgUnit)
{
   CreateUnitWithProperties(count, Unit, dwrand() % 8 + 33, cp, UnitProperty(burrowed=True));
   SetInvincibility(Enable, Unit, cp, "[Skill]Unit_Wait_ALL");
   MoveUnit(count, Unit, cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
}

function SquareShape(cp : TrgPlayer, count, Unit : TrgUnit, x, y)
{
   f.MoveLoc(f.heroID[cp], cp, x, y);
   SkillUnitBurrowed(cp, count, Unit);
   f.MoveLoc(f.heroID[cp], cp, -y, x);
   SkillUnitBurrowed(cp, count, Unit);
   f.MoveLoc(f.heroID[cp], cp, -x, -y);
   SkillUnitBurrowed(cp, count, Unit);
   f.MoveLoc(f.heroID[cp], cp, y, -x);
   SkillUnitBurrowed(cp, count, Unit);
}

function EdgeShapeBurrowed(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval)
{
   var i = 0;

   f.Table_Sin(cp, degree, interval * 14 / 10);
   f.Table_Cos(cp, degree, interval * 14 / 10);

   var x_o = f.CosAngle[cp];
   var y_o = f.SinAngle[cp];

   var distance = (interval * 2) / (n - 1);

   f.Table_Sin(cp, degree + 45, distance);
   f.Table_Cos(cp, degree + 45, distance);

   var distance_x = f.CosAngle[cp];
   var distance_y = f.SinAngle[cp];
   
   if (n > 1)
   {
      for (; i < n - 1; i++)
      {
         SquareShape(cp, 1, Unit, x_o - (distance_x * i), y_o - (distance_y * i));
      }
   }
}