import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);

function main(cp)
{
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("ComputerAlliy", Set);
            SetAllianceStatus(P1, Ally);
            SetAllianceStatus(P2, Ally);
            SetAllianceStatus(P3, Ally);
            SetAllianceStatus(P4, Ally);
            SetAllianceStatus(P5, Ally);
            SetAllianceStatus(P6, Ally);
         }

         if (f.loop[cp] < 10)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            EdgeShapeAt(cp, 1, "Target", 22, 3, 32, 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 1)
         {
            EdgeShapeAt(cp, 1, "Kakaru (Twilight)", 22, 3, 32, 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 5)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 6)
         {
            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 0, 1 + 2 * f.loop[cp], 50 * f.loop[cp]);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 1 + 2 * f.loop[cp], 50 * f.loop[cp]);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 5)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "60 + 1n Siege", 0, 3, 50, x, y);
            }
         }
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 15)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

         if (f.loop[cp] < 6)
         {
            var x = -50 - 50 * f.loop[cp];
            var y = 250 - 50 * f.loop[cp];

            EdgeShapeAt(cp, 1, "50 + 1n Battlecruiser", 0, 3, 50, x, y);
            EdgeShapeAt(cp, 1, "50 + 1n Tank", 0, 3, 50, x, y);

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 11)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 0)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "40 + 1n Gantrithor", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Hydralisk", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 3, 50, x, y);
            }

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n Hydralisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Hydralisk", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 2)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "80 + 1n Artanis", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 3, 50, x, y);
            }
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "40 + 1n Gantrithor", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 3, 50, x, y);
            }

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "80 + 1n Artanis", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 3, 50, x, y);
            }
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "Kakaru (Twilight)", 0, 3, 50, x, y);
            }
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            SetSwitch("ComputerAlliy", Clear);

            if (cp < 3)
            {
               SetAllianceStatus(P4, Enemy);
               SetAllianceStatus(P5, Enemy);
               SetAllianceStatus(P6, Enemy);
            }
            else if (cp >= 3)
            {
               SetAllianceStatus(P1, Enemy);
               SetAllianceStatus(P2, Enemy);
               SetAllianceStatus(P3, Enemy);
            }

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         if (Bring(cp, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill") 
         && Deaths(cp, AtLeast, f.UltimateB[cp], " `UltimateCoolTime"))
         {
            f.Voice_Routine(cp, 3);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 320;
            SetDeaths(cp, Subtract, f.UltimateB[cp], " `UltimateCoolTime");
            KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", cp);
         }
         else
         {
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", cp);
            SetSwitch("UiltimateSwitch", Clear);
            f.SkillEnd(cp);
         }
      }
   }
}

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y)
{
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, x, y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -x, -y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -y, x);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, y, -x);

   f.DotShape(cp, count, Unit, x, y);
   f.DotShape(cp, count, Unit, -x, -y);
   f.DotShape(cp, count, Unit, -y, x);
   f.DotShape(cp, count, Unit, y, -x);
}

