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
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 100);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 100, 100);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
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
            f.SquareShape(cp, 1, "Protoss Dark Archon", 100, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 1)
         {
            EdgeShapeAt(cp, 1, "Terran Science Vessel", 22, 3, 32, 100, 100);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 100, 100);
            KillUnitAt(All, "Terran Science Vessel", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
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
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 0, 1 + 2 * f.loop[cp], 50 * f.loop[cp]);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 1 + 2 * f.loop[cp], 50 * f.loop[cp]);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 5)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "40 + 1n Firebat", 0, 3, 50, x, y);
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

               EdgeShapeAt(cp, 1, "50 + 1n Battlecruiser", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "40 + 1n Wraith", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "Protoss Dark Archon", 0, 3, 50, x, y);
            }

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Wraith", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            MoveUnit(All, "40 + 1n Firebat", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Firebat", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 2)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "80 + 1n Tom Kazansky", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "Protoss Dark Archon", 0, 3, 50, x, y);
            }
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "50 + 1n Battlecruiser", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "Protoss Dark Archon", 0, 3, 50, x, y);
            }

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "80 + 1n Tom Kazansky", 0, 3, 50, x, y);
               EdgeShapeAt(cp, 1, "Protoss Dark Archon", 0, 3, 50, x, y);
            }
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            for (var i = 0; i < 3; i++)
            {
               var x = -0 - 100 * i;
               var y = 300 - 100 * i;

               EdgeShapeAt(cp, 1, "Terran Science Vessel", 0, 3, 50, x, y);
            }
            KillUnitAt(All, "Terran Science Vessel", "Anywhere", cp);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 100)
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
         if (Bring(cp, AtLeast, 20, "Protoss Arbiter", "[Skill]UseSkill") 
         && Deaths(cp, AtLeast, f.UltimateB[cp], " `UltimateCoolTime"))
         {
            f.Voice_Routine(cp, 3);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 0;
            SetDeaths(cp, Subtract, f.UltimateB[cp], " `UltimateCoolTime");
            KillUnitAt(20, "Protoss Arbiter", "[Skill]UseSkill", cp);
         }
         else
         {
            KillUnitAt(All, "40 + 1n Firebat", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
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

